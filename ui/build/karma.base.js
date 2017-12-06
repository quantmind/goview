module.exports = {

    phantomjsLauncher: {
        exitOnResourceError: true
    },

    basePath: '../../',
    singleRun: true,
    frameworks: ['jasmine', 'browserify', 'es5-shim'],

    files: [
        './node_modules/babel-polyfill/dist/polyfill.js',
        './ui/tests/test-*.js'
    ],

    preprocessors: {
        './ui/tests/*.js': ['browserify']
    },

    browserify: {
        debug: true,
        transform: ['babelify']
    },

    customLaunchers: {
        ChromeNoSandbox: {
            base: 'Chrome',
            flags: ['--no-sandbox']
        }
    }
};
