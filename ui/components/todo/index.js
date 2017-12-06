import {assign} from 'd3-let';

import client from '../../client';


export default {
    model () {
        return {
            placeholder: "What needs to be done?",
            newTodo: "",
            todos: [],
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
                    client.post('/api/todos', {text: this.$event.currentTarget.value}).then(entry => {
                        var todos = this.todos.slice();
                        todos.push(getTodo(entry));
                        this.newTodo = '';
                        this.todos = todos;
                    });
                }
            },
            $clear () {
                if (this.$event) this.$event.preventDefault();
                var todos = this.todos.reduce(function (t, todo) {
                    if (!todo.done) t.push(todo);
                    else client.delete('/api/todos', todo.id);
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
                client.patch('/api/todos', item.id, {text: this.$event.currentTarget.value}).then((entry) => {
                    assign(item, entry);
                    item.edit = false;
                });
            }
        };
    },
    render () {
        var model = this.model;
        client.get('/api/todos').then(data => {
            model.todos = data.map(getTodo);
        });
        return this.renderFromUrl('/template/todo');
    }
};


function getTodo (todo) {
    return assign({edit: false}, todo);
}

function count (todos) {
    return todos.reduce(function (c, t) {
        return c + !t.done;
    }, 0);
}
