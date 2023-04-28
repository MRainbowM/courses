console.log('sddsdsdsd');


export function onClickModuleMenu() {
    console.log('111111');
    let moduleMenuPreview = document.getElementById('moduleMenuPreview');
    let moduleMenu = document.getElementById('moduleMenu');




    moduleMenuPreview.onclick = function () {
        console.log('click');
        if (moduleMenu) {
            if (moduleMenu.classList.contains('show')) {
                moduleMenu.classList.remove('show');
            } else {
                moduleMenu.classList.add('show');
            }
        }
    };

}


