import goView from './main';

import {viewProviders} from 'd3-view';

export const goapp = goView();

export function start () {
    viewProviders.Handlebars = this;
    goapp.mount('body');
}
