import PySimpleGUI as sg
from contract_parser import *

payable = False

def main():

    basic_mutations = {
    "state": ["view", "pure"],
    "visibility": ["internal", "external", "public", "private"],
    "data-location": ["storage", "memory"],
    "int-types": ["int", "int8", "int32", "int64", "int128", "int256",
                  "uint", "uint8", "uint32", "uint64", "uint128", "uint256"],
    "math-functions": ["addmod", "mulmod"],
    "address-variable": ["block.coinbase", "msg.sender", "tx.origin"],
    "ether-units": ["wei", "finney", "szabo", "ehter"],
    "time-units": ["seconds", "minutes", "hours", "days", "weeks"],
    "bin-arithmetic": ["+", "-", "*", "/", "%"],
    "relational-operator": [">=", "<=", "==", "!=", ">", "<"],
    "bin-condition": ["&&", "||", "&", "|"],
    "shortcut-asignment": ["+=", "-=", "*=", "/=", "&="]
    }
    extra_mutations = {
    "shortcut-arithmetic": ["++", "--"]
    }
    remove_line_mutations = ['delete', 'require']
    global payable
    contract_path = ''

    names = list(basic_mutations.keys()) + list(extra_mutations.keys()) + remove_line_mutations + ['payable']

    layout = [
        [
            sg.Text("Contract File:"),
            sg.In(enable_events=True, key="-INPUT-"),
            sg.FileBrowse() 
        ],
        [sg.Listbox(values=names, size=(30, 6), key='-LIST-', enable_events=True)],
        [sg.Button('Remove Selected', key='-REMOVE-'), sg.Button('Submit', key='-SUBMIT-'), sg.Button('Exit')],
    ]

    window = sg.Window('Choosing Operators', layout)
    while True:
        event, values = window.read()
            
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == "-INPUT-":
            contract_path = values["-INPUT-"]
        
        if event == '-REMOVE-':
            selected_value = values['-LIST-'][0] if values['-LIST-'] else None
            selected_index = names.index(selected_value)
            if selected_index:
                del names[selected_index]
                window['-LIST-'].update(values=names)

        if event == '-SUBMIT-':

            new_basic_mutations = basic_mutations.copy()
            for key in basic_mutations.keys():
                if key not in names:
                    del new_basic_mutations[key]
                    
            new_extra_mutations = extra_mutations.copy()
            for key in extra_mutations.keys():
                if key not in names:
                    del new_extra_mutations[key]

            new_remove_line_mutations = remove_line_mutations.copy()
            for value in remove_line_mutations:
                if value not in names:
                    new_remove_line_mutations.remove(value)

            if "payable" not in names:
                payable = False
        
            parser = ContractParser(new_basic_mutations, new_extra_mutations, new_remove_line_mutations, payable)
            parser.create_tree(contract_path)


            
    window.close()

if __name__ == '__main__':
    main()
   
