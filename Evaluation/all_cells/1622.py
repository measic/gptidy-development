import datetime as dt
import time
import logging as log
from multiprocessing import Pool, TimeoutError
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from IPython.display import display

%run BreakSectionManager.ipynb
%run Util.ipynb
%run Constant.ipynb
%run Metric.ipynb
%run Operation.ipynb
%run Account.ipynb
%run Policy_Loader.ipynb
%run Evaluation.ipynb
%run AssetPainter.ipynb


class RocketRegression:
    
    def __init__(self, policy_name):
        self.policy_name = policy_name
        self.policy_loader = Policy_Loader(self.policy_name)
        self.debug = self.policy_loader.enabled_log_debug()
        self.context = self.policy_loader.get_context()
        
        self.level = self.context['level']
        self.short = self.context['short']
        self.mid = self.context['mid']
       
        
    def build_operation_file_path(self,symbol,regression_end_date):
        return single_operations_report+'operations_'+symbol+'_'+str(self.short)+'_'+str(self.mid)+'_'+self.level+'_'+regression_end_date+'_'+operation_version+'.csv'
    
    def build_deal_file_path(self,symbol,regression_end_date):
        return single_deals_report+'deals_'+symbol+'_'+str(self.short)+'_'+str(self.mid)+'_'+self.level+'_'+regression_end_date+'_'+operation_version+'.csv'
        
    def build_asset_file_path(self,symbol,regression_end_date):
        return single_asset_report+'account_asset_'+symbol+'_'+str(self.short)+'_'+str(self.mid)+'_'+self.level+'_'+regression_end_date+'_'+operation_version+'.csv'
    
    def persist(self,account,operation_df,symbol,regression_end_date):
        account.get_asset_df().to_csv(self.build_asset_file_path(symbol,regression_end_date),index=False)
        account.deal_df.to_csv(self.build_deal_file_path(symbol,regression_end_date),index=False)
        operation_df.to_csv(self.build_operation_file_path(symbol,regression_end_date), index=False)
        
    def draw_asset(self,symbol,regression_end_date):
        if(self.policy_loader.enable_painter()==True):
            painter = AssetPainter()

            asset_file = self.build_asset_file_path(symbol,regression_end_date)
            painter.draw_month_profit_bars(asset_file)
            painter.draw_audit_asset_bars(asset_file)

            operation_file=self.build_operation_file_path(symbol,regression_end_date)
            painter.draw_operation_asset_bars(operation_file)
    
    def start_regression_on_one_stock(self,symbol,regression_end_date):
        start = time.time()
        sectionManager = BreakSectionManager(symbol,self.context)
        section_df = sectionManager.get_all_break_sections()
        section_df = section_df[section_df['d_s_datetime']<to_datetime(regression_end_date)]
        display(section_df)
        
        metric = Metric(symbol,self.context)
        
        stock_start_date = metric.get_stock_start_date()
        stock_end_date = metric.get_stock_end_date()
        log.info('stock_start_date ' + stock_start_date+' stock_end_date:'+stock_end_date)

        account = Account(self.context,self.policy_name)
        operation = Operation(account,symbol,self.context,self.policy_name)
        
        for key,row in section_df.iterrows():
            start_date = row['d_s_date']
            end_date = row['d_e_date']
            
            start_datetime = to_datetime(start_date)
            end_datetime = to_datetime(end_date)

            buy_price = metric.get_cur_price(start_date)
            
            if(self.debug==True):
                print('\n'+row['symbol']+' section '+start_date+'===>'+end_date)
            while(start_datetime<=end_datetime):
                cur_date = start_datetime.strftime(YMD_format)
                
                if(metric.is_today_open(cur_date)):
                    account.daily_audit(cur_date)

                    if(account.can_open_new_stock()==True):
                        if(operation.is_buy_point(cur_date)==True):
                            operation.open_opsition(cur_date)

                    if(account.has_shares()==True):
                        if(operation.is_sell_point(cur_date)==True):
                            operation.sell_stock(cur_date)

                start_datetime += dt.timedelta(days = 1)
                
        operation_df = operation.get_operations()
        self.persist(account,operation_df,symbol,regression_end_date)
        self.draw_asset(symbol,regression_end_date)
        
        evaluation = Evaluation(account,self.context,self.policy_name)
        evaluation_df = evaluation.get_evaluation_report(symbol,stock_start_date,stock_end_date,
                                                         operation_df)

        end = time.time()
        if(self.debug==False):
            print(symbol+' regression cost time ' + str(round(end-start,1))+' seconds')
        return evaluation_df
    
    
    def start_sync_regression(self,scale,regression_end_date):
        evaluation_df = pd.DataFrame(columns=evaluation_columns)
        symbols = get_symbols(scale,home)
        total = len(symbols) 
        
        for symbol in symbols:
            one_evaluation = self.start_regression_on_one_stock(symbol,regression_end_date)
            evaluation_df = pd.concat([one_evaluation,evaluation_df], ignore_index=True, sort=False)
           
        
        evaluation_df['loss_times'] =evaluation_df['loss_times'].astype('int')
        evaluation_df['deal_count'] =evaluation_df['deal_count'].astype('int')
        evaluation_df['rar'] =evaluation_df['rar'].astype('float')

        return evaluation_df
    
    def start_regression(self,scale,regression_end_date,process_num):
        print('context:' + str(self.context))
        
        if(process_num==1):
            return self.start_sync_regression(scale,regression_end_date)
        
        evaluation_df = pd.DataFrame(columns=evaluation_columns)
        symbols = get_symbols(scale,home)
        total = len(symbols) 
        
        pool = Pool(processes=process_num)
        tasks = []
        for symbol in symbols:
            task = pool.apply_async(self.start_regression_on_one_stock, (symbol,regression_end_date))
            tasks.append(task)
            
        for task in tasks:
            try:
                one_evaluation = task.get()
                evaluation_df = pd.concat([one_evaluation,evaluation_df], ignore_index=True, sort=False)
            except Exception as e:
                print(str(e))
        
        pool.close()
        pool.join()
        
        evaluation_df['loss_times'] =evaluation_df['loss_times'].astype('int')
        evaluation_df['deal_count'] =evaluation_df['deal_count'].astype('int')
        evaluation_df['rar'] =evaluation_df['rar'].astype('float')

        return evaluation_df
    