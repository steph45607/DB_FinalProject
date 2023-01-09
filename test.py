    Label(
        root,
        font=(myFont, 15),
        text="Search By Title : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.02, rely=0.18)
    searchUser = StringVar()
    
    searchInput = Entry(root, textvariable=searchUser, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.19, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchTitle_book(transactionView, searchUser),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.525, rely=0.188)

    refreshBookBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:refreshDisplay_book(searchUser, transactionView),
        font=(myFont, 9),
    )
    refreshBookBtn.place(relx=0.585, rely=0.188)

    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id"
    )
    transactions = cursor.fetchall()

    transactionView = ttk.Treeview(root, selectmode="browse", height=5)
    transactionView.place(relx=0.024, rely=0.25)
    transactionView["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    transactionView["show"] = "headings"
    transactionView.column("1", width=50)
    transactionView.column("2", width=160)
    transactionView.column("3", width=115)
    transactionView.column("4", width=115)
    transactionView.column("5", width=150)
    transactionView.column("6", width=100)
    transactionView.column("7", width=100)
    transactionView.heading("1", text="ID")
    transactionView.heading("2", text="Book Title")
    transactionView.heading("3", text="Borrower ID")
    transactionView.heading("4", text="Borrower Name")
    transactionView.heading("5", text="Date")
    transactionView.heading("6", text="Due")
    transactionView.heading("7", text="Status")

    for i in transactions:  # type: ignore
        # print(i)
        transactionView.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )