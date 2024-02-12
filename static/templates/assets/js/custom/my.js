
var stepperEl = document.querySelector("#kt_stepper_example_basic");
var options = { startIndex: 1 };
var stepper = new KTStepper(stepperEl, options);

var name_u
var theme_u
var url_get

//Скрыть ошибку
function hide() {
    document.getElementById('name-alert').style.display = 'none';
}

//Ошибка при вводе пустого значения
function set_name(name) {
    if (name == "") {
        var elem = document.getElementById('name-alert');
        elem.innerHTML = "<div class='alert alert-primary'><i class='bi bi-droplet-half text-danger fs-3x'></i><div class='d-flex flex-column'><h4 class='mb-1 text-dark'>Пустое значение имени!</h4><span>Повторите ввод</span></div></div>";
        setTimeout(hide, 3000);
    } else {
        stepper.goTo(2);
    }
    name_u = name
}

//Сохранение выбранной темы
function set_theme(theme) {
    stepper.goTo(3);
    theme_u = theme
    let name_attr = document.querySelector('#kt_clipboard');
    url_get = "http://127.0.0.1:8000/?user_name="+name_u+"&theme="+theme_u
    name_attr.value = '[![Codewars]('+url_get+')](https://github.com/pogudo-e/pillow_cw)';
    paste()
    return url_get
}

// Вставка итогового изображения
function paste() {
    var imane = document.getElementById('pasteImage');
    imane.innerHTML = "<img class='' alt='' src='"+url_get+"'/>";
    setTimeout(hide, 3000);
    
}

// Сохранение введенного имени
(function () {
    var adduser_input = document.getElementById('set_name');
    document.getElementById('name_btn').addEventListener('click', call_add);
    function call_add() {
        return set_name(adduser_input.value);
    }
})();


// Select elements
const target = document.getElementById('kt_clipboard');
const button = target.nextElementSibling;

var clipboard = new ClipboardJS(button, {
    target: target,
    text: function () {
        return target.value;
    }
});

// Success action handler
clipboard.on('success', function (e) {
    const currentLabel = button.innerHTML;

    // Exit label update when already in progress
    if (button.innerHTML === 'Скопировано!') {
        return;
    }

    // Update button label
    button.innerHTML = 'Скопировано!';

    // Revert button label after 3 seconds
    setTimeout(function () {
        button.innerHTML = currentLabel;
    }, 3000)
});

