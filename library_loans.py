# Assign `registered_members` to a list of library member names
registered_members = ["jdoe", "msmith", "fjohnson", "dwilliams", "abrown"]

# Assign `loaned_books` to a list of book IDs that correspond to the members in `registered_members`
loaned_books = ["bk1001", "bk2053", "bk3145", "bk4206", "bk5290"]

# Define a function named `loan_status` that takes in two parameters, `member_name` and `book_id`


def loan_status(member_name, book_id):

    # If `member_name` belongs to `registered_members`,
    if member_name in registered_members:

        # then display "The member ______ has an active membership.",
        print("The member", member_name, "has an active membership.")

        # assign `ind` to the index of `member_name` in `registered_members`,
        ind = registered_members.index(member_name)

        # and execute the following conditional
        # If `book_id` matches the element at the index `ind` in `loaned_books`,
        if book_id == loaned_books[ind]:

            # then display "______ has currently loaned the book with ID ______"
            print(member_name, "has currently loaned the book with ID", book_id)

        # Otherwise,
        else:

            # display "______ has not loaned the book with ID ______"
            print(member_name, "has not loaned the book with ID", book_id)

    # Otherwise (part of the outer conditional and handles the case when `member_name` does not belong to `registered_members`),
    else:

        # Display "The member ______ does not have an active membership."
        print("The member", member_name, "does not have an active membership.")


# Call the function to test with different member and book ID combinations
loan_status("msmith", "bk2053")
loan_status("jdoe", "bk4004")
loan_status("kwilson", "bk3145")
