import {viewProviders, jsonResponse} from 'd3-view';


export default {
    get (path, id) {
        if (id) path = `${path}/${id}`;
        return this.json(path, 'GET');
    },

    post (path, data) {
        return this.json(path, 'POST', {body: data});
    },

    patch (path, id, data) {
        return this.json(`${path}/${id}`, 'PATCH', {body: data});
    },

    delete (path, id) {
        var options = this.getOptions('DELETE'),
            fetch = viewProviders.fetch;
        return fetch(`${path}/${id}`, options);
    },

    json (path, method, options) {
        options = this.getOptions(method, options);
        if (options.body) {
            options.body = JSON.stringify(options.body);
            options.headers['Content-Type'] = 'application/json';
        }
        var fetch = viewProviders.fetch;
        return fetch(path, options).then(jsonResponse);
    },

    getOptions (method, options) {
        if (!options) options = {};
        if (!options.headers) options.headers = {};
        if (this.token)
            options.headers['Athorization'] === `Bearer ${this.token}`;
        options.method = method;
        return options;
    }
};
