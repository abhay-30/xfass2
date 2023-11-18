from azure.storage.queue import QueueClient
import json
from python.src.utils.classes.commons.serwo_objects import SerWOObject
import os, uuid


connect_str = "DefaultEndpointsProtocol=https;AccountName=xfaasstoragenew;AccountKey=11K8CXAPwBkXxGHm8TmkohWNEuoz6bpCCjTYoJYcK2sLfJC+ypHSy6JoxB2RLlaX2fVZ378tTZ9m+AStf6MeRA==;EndpointSuffix=core.windows.net"
queue_name = "aws-graph-war"

queue = QueueClient.from_connection_string(conn_str=connect_str, queue_name=queue_name)


def user_function(serwoObject) -> SerWOObject:
    try:
        fin_dict = dict()
        data = serwoObject.get_body()
        print("Data to push - ", data)
        metadata = serwoObject.get_metadata()
        fin_dict["data"] = "success: OK"
        fin_dict["metadata"] = metadata
        print("Fin dict - ", fin_dict)
        queue.send_message(json.dumps(fin_dict))
        print('message sent fin dict func.py *********************************************************************************')
        return SerWOObject(body=data)
    except Exception as e:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return SerWOObject(error=True)
