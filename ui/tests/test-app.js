import goView from '../main';
import {test} from './utils';


describe('fluidily core', function() {


    it('Main application', () => {
        var vm = goView();
        expect(vm).toBeTruthy();
        expect(vm.isMounted).toBeUndefined();
    });

    test('Main application mount', async () => {
        var vm = goView();
        await vm.mount(vm.viewElement('<div></div>'));
        expect(vm.isMounted).toBe(true);
    });

});
