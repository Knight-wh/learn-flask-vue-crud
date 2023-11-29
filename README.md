# Developing a Single Page App with Flask and Vue.js

### TODO

- [ ] Add proper error handling on both the front and back-end.
- [ ] Write an automated test for this
- [x] Handle an invalid payload where the `title`, `author`, and/or `read` is missing
- [ ] Think of any potential errors on the client or server
- [x] Think about where `showMessage` should be set to `false`.
- [x] Try using the Alert component to display errors.
- [x] Refactor the alert to be dismissible.
- [ ] Handle the case of an `id` not existing.
- [ ] Refactor the for loop in the remove_book so that it's more Pythonic.
- [ ] Clean the component up by moving the methods that make HTTP calls to a untils or services file.
- [ ] Try to combine some of the methods that contain similar logic, like `handleAddSumit` and `handleEditSubmit`.
- [ ] Instead of deleting on the button click, add a confimation alert.
- [x] Display a "No books! Please add one." message when no books are present in the table.

### Want to learn how to build this?

Check out the [tutorial](https://testdriven.io/developing-a-single-page-app-with-flask-and-vuejs).

## Want to use this project?

1. Fork/Clone

1. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd server
    $ python3 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ flask run --port=5001 --debug
    ```

    Navigate to [http://localhost:5001](http://localhost:5001)

1. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run dev
    ```

    Navigate to [http://localhost:5173](http://localhost:5173)
