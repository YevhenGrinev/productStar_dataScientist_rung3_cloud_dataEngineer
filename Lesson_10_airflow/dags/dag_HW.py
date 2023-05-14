from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta

from airflow.operators.bash import BashOperator
from  airflow.operators.python import PythonOperator

default_arguments = {
    'owner': 'evgenijgrinev',
}

with DAG(
    'dag_HW',
    schedule_interval=timedelta(days=1),
    catchup=False,
    default_args=default_arguments,
    start_date=days_ago(1),
) as dag:

    def check_txt():
        import os

        list_txt = []
        directory = '/Users/evgenijgrinev/airflow/test'
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                list_txt.append(filename)

        from collections import Counter
        import re

        if list_txt != 0:
            lst = []
            for i in range(len(list_txt)):
                f = open(f"/Users/evgenijgrinev/airflow/test/{list_txt[i]}")
                fd = f.read()
                counts =  Counter(re.findall('\w+', fd))
                lst.append(counts)

            f = open("/Users/evgenijgrinev/airflow/test/file_to_s3/updated.txt", "w+")
            string = ''
            for el in lst:
                string += str(el)
                string += ' '
            f.write(string)
        else: 
            pass


    op1 = PythonOperator(
        task_id='check_py',
        python_callable=check_txt
    )

    op2 = BashOperator(
        task_id="create_bucket",
        bash_command="aws --endpoint-url=https://storage.yandexcloud.net s3 mb s3://bucket-123456"
    )

    op3 = BashOperator(
        task_id="download_file",
        bash_command="aws --endpoint-url=https://storage.yandexcloud.net s3 cp --recursive ~/airflow/test/file_to_s3 s3://bucket-123456/updated"
    )

    op4 = BashOperator(
        task_id="access",
        bash_command="aws --endpoint-url=https://storage.yandexcloud.net s3api put-object-acl --bucket bucket-123456 --key updated/updated.txt --acl public-read"
    )

    op5 = BashOperator(
        task_id="move",
        bash_command="mv ~/airflow/test/*.txt ~/airflow/test/output/"
    )

op1 >> op2 >> op3 >> op4 >> op5 