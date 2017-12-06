//  Create d3 View
//
import {view} from 'd3-view';

import components from './components';


export default function () {

    // Build the model-view pair
    var vm = view({
        model: {}
    });

    //
    vm.use(components);

    return vm;
}
