class Preprocessor:

    def __init__(self, train_data_file, train_label_file, train_ids_file,
                 instr_file, test_data_file=None, test_ids_file=None):
        """A class to process and reformat data
        for use in learning models"""

        # initialize the data the data filenames
        self.train_data_file = train_data_file
        self.train_label_file = train_label_file
        self.train_ids_file = train_ids_file
        self.instr_file = instr_file

        # test data is optional
        self.test_data_file = test_data_file
        self.test_ids_file = test_ids_file

    def read_data(self):
        """Reads in data from the files passed to constructor"""

        # read in the data
        train_X_df = pd.read_csv(self.train_data_file)
        train_y_df = pd.read_csv(self.train_label_file)
        train_ids_df = pd.read_csv(self.train_ids_file)
        self.instr_df = pd.read_csv(self.instr_file)

        self.feature_names = [feature for feature in train_X_df]
        self.original_feature_names = [feature for feature in train_X_df]
        self.label_names = [feature for feature in train_y_df]
        self.id_names = [feature for feature in train_ids_df]

        # create cross validation data
        self.cv_X_df = pd.DataFrame(train_X_df)
        self.cv_y_df = pd.DataFrame(train_y_df)
        self.cv_ids_df = pd.DataFrame(train_ids_df)

        # read in the test data if it exists
        if self.test_data_file is not None:
            self.test_X_df = pd.read_csv(self.test_data_file)
            self.test_ids_df = pd.read_csv(self.test_ids_file)
            self.all_X_df = train_X_df.append(self.test_X_df)
        else:
            self.test_X_df = None
            self.test_ids_df = None
            self.all_X_df = pd.DataFrame(train_X_df)

        # determine the shape of the input data
        self.train_X_shape = train_X_df.shape
        self.train_y_shape = train_y_df.shape
        self.train_ids_shape = train_ids_df.shape
        self.instr_shape = self.instr_df.shape
        self.all_shape = self.all_X_df.shape

        # get size of test data if it exists
        if self.test_data_file is not None:
            self.test_X_shape = self.test_X_df.shape
            self.test_ids_shape = self.test_ids_df.shape
        else:
            self.test_X_shape = None
            self.test_ids_shape = None

    def process(self, shuffle_train_data=False):
        """Performs the processing on cross validation and train/test data"""

        # ADD OPTION TO SHUFFLE DATA HERE

        # processing on all data - remember to include cv_X and all_X for each condition
        for col in self.original_feature_names:
            print(col)

            # determine what to perform at each of the steps
            col_instr = self.instr_df[col].values
            col_enc = col_instr[1]
            col_scl = col_instr[2]
            col_imp = col_instr[3]

            # impute values
            # imputed first so that other functions will not use nan values in calculations
            if col_imp == 'UNIQ':
                self.cv_X_df[col] = UNIQ(self.cv_X_df[col], value=-1)
                self.all_X_df[col] = UNIQ(self.all_X_df[col], value=-1)
            if col_imp == 'MEAN':
                self.cv_X_df[col] = MEAN(self.cv_X_df[col])
                self.all_X_df[col] = MEAN(self.all_X_df[col])
            if col_imp == 'MODE':
                self.cv_X_df[col] = MODE(self.cv_X_df[col])
                self.all_X_df[col] = MODE(self.all_X_df[col])
            if col_imp == 'MED':
                self.cv_X_df[col] = MED(self.cv_X_df[col])
                self.all_X_df[col] = MED(self.all_X_df[col])
            if is_int(col_imp):
                self.cv_X_df[col] = CONST(self.cv_X_df[col], col_imp)
                self.all_X_df[col] = CONST(self.all_X_df[col], col_imp)
            if col_imp == 'DEL':
                self.cv_X_df, self.all_X_df, self.feature_names = DEL(
                    self.cv_X_df, self.all_X_df, col, self.feature_names)

            # perform encoding of data
            if col_enc == 'MAP':
                self.cv_X_df[col] = MAP(self.cv_X_df[col])
                self.all_X_df[col] = MAP(self.all_X_df[col])
            if col_enc == 'OHE':
                self.cv_X_df, self.all_X_df, self.feature_names = OHE(
                    df_cv=self.cv_X_df, df_all=self.all_X_df, col_name=col,
                    feature_names=self.feature_names)
            if col_enc == 'LOO':
                self.cv_X_df[col] = LOO(self.cv_X_df[col])
                self.all_X_df[col] = LOO(self.all_X_df[col])

            # perform scaling
            if col_scl == 'NRM1':
                self.cv_X_df[col] = NRM1(self.cv_X_df[col])
                self.all_X_df[col] = NRM1(self.all_X_df[col])
            if col_scl == 'SCL1':
                self.cv_X_df[col] = SCL1(self.cv_X_df[col])
                self.all_X_df[col] = SCL1(self.all_X_df[col])
            if col_scl == 'TRSH':
                self.cv_X_df[col] = TRSH(self.cv_X_df[col])
                self.all_X_df[col] = TRSH(self.all_X_df[col])

        # get the values from the dataframes
        self.cv_X = self.cv_X_df.values
        self.cv_y = self.cv_y_df.values
        self.cv_ids = self.cv_ids_df.values

        all_X = self.all_X_df.values
        self.train_X = all_X[:self.train_X_shape[0], :]
        self.train_y = self.cv_y_df.values
        self.train_ids = self.cv_ids_df.values

        if self.test_data_file is not None:
            self.test_X = all_X[self.train_X_shape[0]:, :]
            self.test_ids = self.test_ids_df.values
        else:
            self.test_X = None
            self.test_ids = None

    def write_data(self, out_dir='./processed_data/'):
        """Writes all of the data to output files"""

        # create the output directory if it does not exist
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        # convert arrays back into DataFrames
        cv_X_df = pd.DataFrame(self.cv_X, columns=self.feature_names)
        cv_y_df = pd.DataFrame(self.cv_y, columns=self.label_names)
        cv_ids_df = pd.DataFrame(self.cv_ids, columns=self.id_names)
        train_X_df = pd.DataFrame(self.train_X, columns=self.feature_names)
        train_y_df = pd.DataFrame(self.train_y, columns=self.label_names)
        train_ids_df = pd.DataFrame(self.train_ids, columns=self.id_names)
        if self.test_data_file is not None:
            test_X_df = pd.DataFrame(self.test_X, columns=self.feature_names)
            test_ids_df = pd.DataFrame(self.test_ids, columns=self.id_names)

        # write the dataframes to file
        cv_X_df.to_csv(out_dir + 'cv_X.csv', index=False)
        cv_y_df.to_csv(out_dir + 'cv_y.csv', index=False)
        cv_ids_df.to_csv(out_dir + 'cv_ids.csv', index=False)
        train_X_df.to_csv(out_dir + 'train_X.csv', index=False)
        train_y_df.to_csv(out_dir + 'train_y.csv', index=False)
        train_ids_df.to_csv(out_dir + 'train_ids.csv', index=False)
        if self.test_data_file is not None:
            test_X_df.to_csv(out_dir + 'test_X.csv', index=False)
            test_ids_df.to_csv(out_dir + 'test_ids.csv', index=False)

    def select_features(self):
        """Perform features selection / compression algs like PCA."""
        """These will be implemented once more has been done."""
        self.feature_names = self.feature_names