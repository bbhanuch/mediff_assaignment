# Problem statement: Implement a group_by_owners function that:
# i) Accepts a dictionary containing the file owner name for each file name.
# ii) Returns a dictionary containing a list of file names for each owner name, in any order


def group_by_owners(input_data):
    output_data = {}
    for file_type, owner in input_data.items():
        output_data[owner] = output_data.setdefault(owner, []) + [file_type]
    return output_data


input_data = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(input_data))