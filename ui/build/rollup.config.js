import json from 'rollup-plugin-json';
import babel from 'rollup-plugin-babel';
import commonjs from 'rollup-plugin-commonjs';
import node from 'rollup-plugin-node-resolve';
import sourcemaps from 'rollup-plugin-sourcemaps';


const externalRequires = new Set(['handlebars']);
const externalResolve = new Set(['d3-view', 'd3-visualize']);

const commonPath = ['node_modules/**'];
const pkg = require('../../package.json');
const external = Object.keys(pkg.dependencies).filter(name => {
    return !externalResolve.has(name) && (name.substring(0, 3) === 'd3-' || externalRequires.has(name));
});


export default [
    {
        input: 'ui/index.js',
        external: external,
        output: {
            file: 'static/goview.js',
            format: 'umd',
            name: 'd3',
            sourcemap: true,
            extend: true,
            globals: external.reduce((g, name) => {g[name] = name.substring(0, 3) === 'd3-' ? 'd3' : name; return g;}, {})
        },
        plugins: [
            json(),
            node(),
            babel({
                babelrc: false,
                runtimeHelpers: true,
                presets: ['es2015-rollup']
            }),
            commonjs({include: commonPath}),
            sourcemaps()
        ]
    },
    {
        input: 'ui/require.js',
        output: {
            file: 'build/require.js',
            format: 'umd',
            name: 'd3',
            extend: true
        },
        plugins: [
            json(),
            node(),
            babel({
                babelrc: false,
                runtimeHelpers: true,
                presets: ['es2015-rollup']
            })
        ]
    }
];
