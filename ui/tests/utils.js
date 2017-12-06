import 'es6-promise';
import {viewDebounce} from 'd3-view';

window.handlebars = require('handlebars');

//
//  Return an object with a promise and the resolve function for the promise
export function getWaiter () {
    var waiter = {};
    waiter.promise = new Promise(function (resolve) {
        waiter.resolve = resolve;
    });
    return waiter;
}

export function trigger (target, event, process) {
    var e = document.createEvent('HTMLEvents');
    e.initEvent(event, true, true);
    if (process) process(e);
    target.dispatchEvent(e);
}


export function testAsync (runAsync) {
    return (done) => {
        runAsync().then(done, done.fail);
    };
}

export function test (name, runAsync) {
    return it(name, testAsync(runAsync));
}

export const nextTick = viewDebounce();
