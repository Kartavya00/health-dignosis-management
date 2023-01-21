import tkinter as tk
from tkinter import ttk
import configuredb

#root = tk.Tk()


class CbTreeview(ttk.Treeview):
    def __init__(self, master=None, **kw):
        kw.setdefault('style', 'cb.Treeview')
        kw.setdefault('show', 'headings')  # hide column #0
        ttk.Treeview.__init__(self, master, **kw)
        # create checheckbox images
        self._im_checked = tk.PhotoImage('checked',
                                         data=b'GIF89a\x0e\x00\x0e\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x02#\x04\x82\xa9v\xc8\xef\xdc\x83k\x9ap\xe5\xc4\x99S\x96l^\x83qZ\xd7\x8d$\xa8\xae\x99\x15Zl#\xd3\xa9"\x15\x00;',
                                         master=self)
        self._im_unchecked = tk.PhotoImage('unchecked',
                                           data=b'GIF89a\x0e\x00\x0e\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x0e\x00\x0e\x00\x00\x02\x1e\x04\x82\xa9v\xc1\xdf"|i\xc2j\x19\xce\x06q\xed|\xd2\xe7\x89%yZ^J\x85\x8d\xb2\x00\x05\x00;',
                                           master=self)
        style = ttk.Style(self)
        style.configure("cb.Treeview.Heading", font=("Consolas",10,'bold'))
        # put image on the right
        style.layout('cb.Treeview.Row',
                     [('Treeitem.row', {'sticky': 'nswe'}),
                      ('Treeitem.image', {'side': 'right', 'sticky': 'e'})])

        # use tags to set the checkbox state
        self.tag_configure('checked', image='checked')
        self.tag_configure('unchecked', image='unchecked')

    def tag_add(self, item, tags):
        new_tags = tuple(self.item(item, 'tags')) + tuple(tags)
        self.item(item, tags=new_tags)

    def tag_remove(self, item, tag):
        tags = list(self.item(item, 'tags'))
        tags.remove(tag)
        self.item(item, tags=tags)

    def insert(self, parent, index, iid=None, **kw):
        item = ttk.Treeview.insert(self, parent, index, iid, **kw)
        self.tag_add(item, (item, 'unchecked'))
        self.tag_bind(item, '<ButtonRelease-1>',
                      lambda event: self._on_click(event, item))

    def _on_click(self, event, item):
        """Handle click on items."""
        #curItem = self.focus()
        #print (self.item(curItem))

        #getting selected row in dictionary
        dictvalues = self.item(item)


        rowvalues = dictvalues.get('values')
        pid = rowvalues[0]
        configuredb.selectedpid = pid



        if self.identify_row(event.y) == item:
            
            if self.identify_column(event.x) == '#10': # click in 'Served' column
                # toggle checkbox image
                if self.tag_has('checked', item):
                  
                    self.tag_remove(item, 'checked')
                    self.tag_add(item, ('unchecked',))
                else:
                   
                    self.tag_remove(item, 'unchecked')
                    self.tag_add(item, ('checked',))



'''
tree = CbTreeview(root, columns=("Table No.", "Order", "Time" ,"Served"),
                  height=400, selectmode="extended")

tree.heading('Table No.', text="Table No.", anchor='w')
tree.heading('Order', text="Order", anchor='w')
tree.heading('Time', text="Time", anchor='w')
tree.heading('Served', text="Served", anchor='w')

tree.column('#1', stretch='no', minwidth=0, width=100)
tree.column('#2', stretch='no', minwidth=0, width=600)
tree.column('#3', stretch='no', minwidth=0, width=100)
tree.column('#4', stretch='no', minwidth=0, width=70)

tree.pack(fill='both')

for i in range(1,5):
    tree.insert('', 'end', values=(i, i, i))
root.mainloop()

'''
