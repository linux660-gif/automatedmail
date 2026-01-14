import json

class HandleJson:
        def __init__(self):
                path = None
                file = None

        def update_json(self, current_json_file,form_details_to_update):
                
                try:
                    with open(current_json_file, 'r+') as file:
                        file_data = json.load(file)


                except FileNotFoundError:
                    file_data = []


                except json.JSONDecodeError:
                    file_data = []

                if isinstance(file_data, list):
                       file_data.append(form_details_to_update)

                else:
        
                    print("Error: JSON file does not contain a list/array at the root level.")
                    return

   
                with open(current_json_file, 'w') as file:
                    json.dump(file_data, file, indent=4)
                    

                




       