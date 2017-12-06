

module.exports = {
    out: 'static/goview-require.js',
    prepend: [
        'whatwg-fetch/fetch.js'
    ],
    append: [
        'build/require.js'
    ],
    dependencies: {
        handlebars: {
            main: 'dist/handlebars.min.js'
        }
    }
};
