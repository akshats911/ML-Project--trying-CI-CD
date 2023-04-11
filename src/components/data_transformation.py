# import sys
# from dataclasses import dataclass

# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import OneHotEncoder, StandardScaler
# from sklearn.compose import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline

# from src.exceptions import CustomException
# from src.logger import logging
# import os
# from src.utils import save_object

# df = pd.read_csv(r"artifacts/test.csv")
# # print(df.head())

# @dataclass
# class DataTransformationConfig:
#     preprocessor_obj_file_path:str = os.path.join('artifacts',"preprocessor.pkl")

# class DataTransformation:
#     def __init__(self):
#         self.data_transformation_config=DataTransformationConfig()
    
#     def get_data_transformer_object(self):
#         logging.info("Entered the data transformation method")
#         try:
            
#             num_col = ["writing_score", "reading_score"]
#             cat_col = ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preperation_course"]

#             num_piepline = Pipeline(
#                 steps=[
#                 ("imputer", SimpleImputer(strategy="median")),
#                 ("scaler", StandardScaler()),
#                 ]
#             )

#             cat_pipeline = Pipeline(
#                 steps=[
#                 ("imputer", SimpleImputer(strategy="most_frequent")),
#                 ("onehot", OneHotEncoder(handle_unknown="ignore")),
#                 ("scaler", StandardScaler())
#                 ]
#             )
#             logging.info("categorical columns encoding completed")
#             logging.info("numerical columns scaling completed")

#             preprocessor = ColumnTransformer(
#                 [
#                     ("num_pipeline",num_piepline,num_col),
#                     ("cat_pipeline",cat_pipeline,cat_col)    
#                 ]
#             )
#             return preprocessor
        
#         except Exception as e:
#             raise CustomException(e,sys)
    
#     def initate_data_transformation(self, train_path, test_path):
#         try:
#             train_df = pd.read_csv(train_path)
#             test_df = pd.read_csv(test_path)
#             logging.info("Read train and test data from artifacts folder.")
#             logging.info("obtain preprocessor object")

#             preprocessing_obj = self.get_data_transformer_object()  
#             target_col = "math_score"
#             num_col = ["writing_score", "reading_score"]
#             input_feature_train_df = train_df.drop(columns=[target_col], axis=1)
#             target_feature_train_df = train_df[target_col]

#             input_feature_test_df = test_df.drop(columns=[target_col], axis=1)
#             target_feature_test_df = test_df[target_col]

#             logging.info("Transforming train and test data")

#             input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
#             input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

#             train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
#             test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

#             logging.info("Saved preprocessing object.")

#             save_object(
#                 file_path = self.data_transformation_config.preprocessor_obj_file_path,
#                 obj=preprocessing_obj
#             )

#             return (
#                 train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path
#             )
#         except Exception as e:
#             raise CustomException(e ,sys)
            


import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exceptions import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)


