from airflow.sdk import dag,task


@dag()

def versioned_dag():

    @task.python
    def first_task():
        print('This is the first task')


    @task.python
    def second_task():
        print('This is the second task')

    
    @task.python
    def third_task():
        print('This is the third task. This is the last task in this DAG')

    @task.python
    def versioned_task():
        print('This is the versioned task.No TEST')



    first = first_task()
    second = second_task()
    third = third_task()
    versioned = versioned_task()

    first >> second >> third >> versioned

versioned_dag()

 