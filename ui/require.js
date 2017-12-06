import {version} from '../package.json';

var d3 = window.d3;

d3.require.local('goview', `/static/goview.js?version=${version}`);

d3.require('goview', 'handlebars').then(site => {
    site.start();
});
