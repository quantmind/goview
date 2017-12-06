export default {
    model () {
        return {
            placeholder: "What needs to be done?",
            newTodo: "",
            todos: [todo('something to do'), todo('something else to do')],
            done: {
                reactOn: ['todos'],
                get: function () {
                    return this.todos.length - count(this.todos);
                }
            },
            count: {
                reactOn: ['todos'],
                get: function () {
                    return count(this.todos);
                }
            },
            left: {
                reactOn: ['todos'],
                get: function () {
                    var c = count(this.todos);
                    if (c === 1) return '1 item left';
                    return c + ' items left';
                }
            },
            // Model actions
            $addTodo () {
                if (this.$event && this.$event.keyCode !== 13) return;
                if (this.newTodo) {
                    var todos = this.todos.slice();
                    todos.push(todo(this.newTodo));
                    this.newTodo = '';
                    this.todos = todos;
                }
            },
            $clear () {
                if (this.$event) this.$event.preventDefault();
                var todos = this.todos.reduce(function (t, todo) {
                    if (!todo.done) t.push(todo);
                    return t;
                }, []);
                if (todos.length < this.todos.length) this.todos = todos;
            },
            $toggle (item) {
                item.done = !item.done;
                // trigger a change in todos property
                this.$change('todos');
            },
            $edit (item) {
                if (!item.done) item.edit = true;
            },
            $doneEdit (item) {
                if (this.$event && this.$event.keyCode !== 13) return;
                item.edit = false;
            }
        };
    },
    render () {
        return this.renderFromUrl('./todo.html');
    }
};


function todo (text) {
    return {
        text: text,
        done: false,
        edit: false
    };
}

function count (todos) {
    return todos.reduce(function (c, t) {
        return c + !t.done;
    }, 0);
}
