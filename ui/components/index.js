import todo from './todo';


// d3-view plugin
export default {

    install (vm) {
        vm.addComponent('todo', todo);
    }

};
