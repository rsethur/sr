  
import os
import sys
import argparse

#import dotenv
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

def main():

    #dataset_filename = os.environ.get("DATASET_FILE_NAME", )
    credit_data_df = pd.read_csv("dataset/german_credit_data.csv")   

    clf = model_train(credit_data_df)

    #copying to "outputs" directory, automatically uploads it to azure ml
    output_dir = './outputs/'
    model_name = "aaarisk_model.joblib"
    os.makedirs(output_dir, exist_ok=True)
    joblib.dump(value=clf, filename=output_dir+model_name)


def model_train(credit_data_df):
    #credit_data_df = pd.read_csv("dataset/german_credit_data.csv")  # , nrows=200000, parse_dates=["LEG1_DEP_DATE_GMT", "LEG1_ARR_DATE_GMT","LEG2_DEP_DATE_GMT", "LEG2_ARR_DATE_GMT"])
    credit_data_df.drop("Sno", axis=1, inplace=True)

    y_raw = credit_data_df['Risk']
    X_raw = credit_data_df.drop('Risk', axis=1)
    #del credit_data_df

    categorical_features = X_raw.select_dtypes(include=['object']).columns
    numeric_features = X_raw.select_dtypes(include=['int64', 'float']).columns

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value="missing")),
        ('onehotencoder', OneHotEncoder(categories='auto', sparse=False))])

    numeric_transformer = Pipeline(steps=[
        # ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    feature_engineering_pipeline = ColumnTransformer(
        transformers=[
            ('numeric', numeric_transformer, numeric_features),
            ('categorical', categorical_transformer, categorical_features)
        ], remainder="drop")

    #Encode Labels
    le = LabelEncoder()
    encoded_y = le.fit_transform(y_raw)

    #Train test split
    X_train, X_test, y_train, y_test = train_test_split(X_raw, encoded_y, test_size=0.20, stratify=encoded_y, random_state=42)

    #Create sklearn pipeline
    lr_clf = Pipeline(steps=[('preprocessor', feature_engineering_pipeline),
                             ('classifier', LogisticRegression(solver="lbfgs"))])
    #Train the model
    lr_clf.fit(X_train, y_train)

    #Capture metrics
    train_acc = lr_clf.score(X_train, y_train)
    test_acc = lr_clf.score(X_test, y_test)
    print("training accuracy: %.3f" % train_acc)
    print("test data accuracy: %.3f" % test_acc)

    return lr_clf

if __name__ == "__main__":
    main()