from airflow.sdk import dag,task
from airflow.operators.bash import BashOperator


@dag()

def operators_dag():

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
        print('This is the versioned task')

    @task.bash
    def bash_task_modern():
        return "echo https://airflow.apache.org/"
    
    bash_task_old_school = BashOperator(
    task_id="bash_task_old_school",
    bash_command="echo https://airflow.apache.org/",
)





    first = first_task()
    second = second_task()
    third = third_task()
    versioned = versioned_task()
    bash_modern = bash_task_modern()
    bash_old_school = bash_task_old_school

    first >> second >> third >> versioned >> bash_modern >> bash_old_school 

operators_dag()

 