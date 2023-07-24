pred=definitive_res(z_test.dot(weight))
create_csv_submission(ids_test,pred,"testsubs")