import todo from './todo/index';


// d3-view plugin
export default {

    install (vm) {
        vm.addComponent('todo', todo);
    }

};
