from xml.etree import cElementTree as ET
import tkinter as tk
from tkinter import ttk,Button,Label


class parser:



    def strih_code(self,subelem: object) -> str:
        for i in subelem.findall('{http://v8.1c.ru/8.1/data/enterprise/current-config}Штрихкод'):
            a = i.text
            return a

    def pars_wight(self, subelem: object) -> str:
        for i in subelem.findall('{http://v8.1c.ru/8.1/data/enterprise/current-config}Вес'):
            a = i.text
            return a

    def pars_long(self,subelem: object) -> str:

        for i in subelem.findall('{http://v8.1c.ru/8.1/data/enterprise/current-config}Длина'):
            a = i.text
            return a

    def pars_hight(self, subelem: object) -> str:

        for i in subelem.findall('{http://v8.1c.ru/8.1/data/enterprise/current-config}Высота'):
            a = i.text
            return a


    def pars_name(self, subelem: object) -> str:

        for i in subelem.findall('{http://v8.1c.ru/8.1/data/enterprise/current-config}Description'):
            a = i.text
            return a

    def pars_product(self) -> list:
        list_info = []
        root = ET.parse("may.xml").getroot()
        # print(root.tag)
        for elem in root.findall('{http://www.1c.ru/V8/1CV8DtUD/}Data'):
            print(elem)
            for subelem in elem.findall('{http://v8.1c.ru/8.1/data/enterprise/current-config}CatalogObject.Номенклатура'):
                name = self.pars_name(subelem)
                hight = self.pars_hight(subelem)
                long = self.pars_long(subelem)
                wight = self.pars_wight(subelem)
                strih_code = self.strih_code(subelem)
                loc_list = [name, hight, long, wight, strih_code]
                list_info.append(loc_list)
                print(name, hight, long, wight, strih_code)
        print(list_info)
        return list_info





class interface:
    def __init__(self):
        root = tk.Toplevel()

        def info_heading_tree():
            for i in range(len(list_colum)):
                # a = list_colum[i]
                self.tree.heading(list_colum[i], text=list_colum[i])

        def insert_info_in_tree():
            class_parser = parser()
            list = class_parser.pars_product()
            for i in range(len(list)):
                a = list[i]
                self.tree.insert('', tk.END, values=a)

        def size_tree_colum():
            self.tree.column('Название', width=490)
            self.tree.column('Высота', width=50)
            self.tree.column('Высота', width=50)
            self.tree.column('Длина', width=50)
            self.tree.column('Вес', width=50)
            self.tree.column('Штрих-Код', width=190)

        root.geometry('890x500')
        list_colum = ['Название', 'Высота', 'Длина', 'Вес', 'Штрих-Код']
        self.tree = ttk.Treeview(root, show="headings", columns=list_colum)
        self.tree.place(x=20, y=20)


        info_heading_tree()
        insert_info_in_tree()
        size_tree_colum()
        root.mainloop()

if __name__ == '__main__':
    interface()