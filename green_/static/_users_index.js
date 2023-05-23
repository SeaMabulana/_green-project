const _objectRegister =  {
    first_name : document.forms['registerForm']['first_name'],
    last_name : document.forms['registerForm']['last_name'],
    za_id_number : document.forms['registerForm']['za_id_number'],
    password1 : document.forms['registerForm']['password1'],
    password2 : document.forms['registerForm']['password2']
  }

//Register form array list
const _arrayRegister = [
    document.forms['registerForm']['first_name'], // register[0]
    document.forms['registerForm']['last_name'], // register[1]
    document.forms['registerForm']['za_id_number'], // register[2]
    document.forms['registerForm']['password1'], // register[4]
    document.forms['registerForm']['password2'] // register[5]
]
  
// Rrgister form buttons
const registerButton = {
    register : document.forms['registerForm']['register'],
    submit : document.forms['registerForm']['submit'],
    cancel : document.forms['registerForm']['cancel']
}

// Register form strong password validation box variables
var contextcontainer = document.getElementById('contextcontainer')
var registerLength = document.getElementById('registerLength')
var registerLowercase = document.getElementById('registerLowercase')
var registerUppercase = document.getElementById('registerUppercase')
var registerSplcharacter = document.getElementById('registerSplcharacter')
var registerNumber = document.getElementById('registerNumber')

document.addEventListener('DOMContentLoaded', function() {
    _arrayRegister[0].focus()
})

// When password field focus, show the contextcontainer box
_objectRegister.password1.onfocus = function() {
    contextcontainer.style.display = 'block'
}

// When password field onblar, hide the contextcontainer box
_objectRegister.password1.onblur = function() {
    contextcontainer.style.display = 'none'
}

// password2 disabled is true when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    _objectRegister.first_name.focus();            
    _objectRegister.password2.disabled = true
})


// Register form strong password validate when the user starts to type in password input
_objectRegister.password1.onkeyup = function() {
    // let strongPass = 0
    // Validate lowercase letters
    let lowerCaseLetters = /[a-z]/g;
    if(_objectRegister.password1.value.match(lowerCaseLetters)) {
        registerLowercase.classList.remove('invalid');
        registerLowercase.classList.add('valid');
        // strongPass += 1
    } else {
        registerLowercase.classList.remove('valid');
        registerLowercase.classList.add('invalid');
        // strongPass -= 1
    }
    // Validate capital letters
    let upperCaseLetters = /[A-Z]/g;
    if(_objectRegister.password1.value.match(upperCaseLetters)) {
        registerUppercase.classList.remove('invalid');
        registerUppercase.classList.add('valid');
        // strongPass += 1
    } else {
        registerUppercase.classList.remove('valid');
        registerUppercase.classList.add('invalid');
        // strongPass -= 1
    }
    // Validate numbers
    let numbers = /[0-9]/g;
    if(_objectRegister.password1.value.match(numbers)) {
        registerNumber.classList.remove('invalid');
        registerNumber.classList.add('valid');
        // strongPass += 1
    } else {
        registerNumber.classList.remove('valid');
        registerNumber.classList.add('invalid');
        // strongPass -= 1
    }
    /*
    Validate special character
    [!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+
    [`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]
    */
    let _specialCharacters = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/g;
    if (_objectRegister.password1.value.match(_specialCharacters)) {
        registerSplcharacter.classList.remove('invalid');
        registerSplcharacter.classList.add('valid');
        // strongPass += 1
    } else {
        registerSplcharacter.classList.remove('valid');
        registerSplcharacter.classList.add('invalid');
        // strongPass -= 1
    }
    // Validate length
    if (_objectRegister.password1.value.length >= 8) {
        registerLength.classList.remove('invalid');
        registerLength.classList.add('valid');
        _objectRegister.password2.disabled = false;
        // strongPass += 1
    } else {
        registerLength.classList.remove('valid');
        registerLength.classList.add('invalid');
        // strongPass -= 1
    }
    // strongPass
    // if (strongPass == 5) {
    // _objectRegister.password2.disabled = false;
    // } else {
    // _objectRegister.password2.disabled = true;
    // }
}

// Register keydown event listener to select input to input
_arrayRegister.forEach(function(item, index) {
    item.addEventListener('keydown', function(event) {
    const key = event.key; // 'Enter' 'ArrowUp', 'ArrowDown'
    switch (key) { 
        case 'Enter':
        if (item.name == 'password2') {
            if (item.value == '') {
                event.preventDefault();
                _objectRegister.password2.parentElement.classList.add('empty-fld');
                _objectRegister.password2.focus();
                setTimeout(function() {
                    _objectRegister.password2.parentElement.classList.remove('empty-fld')
                }, 2000);
            } else if (item.value != _objectRegister.password1.value) {
                event.preventDefault();
                _objectRegister.password2.parentElement.classList.add('pswdntmtch');
                _objectRegister.password2.focus();
                setTimeout(function() {
                    _objectRegister.password2.parentElement.classList.remove('pswdntmtch')
                }, 2000);
            } else {
                event.preventDefault();
                registerButton.register.focus()
            }
        } else {
            event.preventDefault();
            _arrayRegister[index+1].focus();
        }
        break;
        case 'ArrowUp':
            event.preventDefault();
            _arrayRegister[index-1].focus();
            break;
            case 'ArrowDown':
            event.preventDefault();
            _arrayRegister[index+1].focus();
            break;
    }
    })
})

// Register Confirm box
const confirmButton = [
    document.forms['registerForm']['submit'],
    document.forms['registerForm']['cancel']
]
confirmButton.forEach(function(item, index) {
    item.addEventListener('mouseover', function() {
        item.focus();
    })
})
confirmButton.forEach(function(item, index) {
    item.addEventListener('mouseout', function() {
        item.blur();
    })
})

// Register form when register button is ckicked check for form empty fields 
registerButton.register.addEventListener('click', function() {
    let registerConfirmbox = document.getElementById('registerConfirmbox')
    if (_objectRegister.first_name.value == '') {
        _objectRegister.first_name.parentElement.classList.add('empty-fld');
        _objectRegister.first_name.focus();
        setTimeout(function() {
            _objectRegister.first_name.parentElement.classList.remove('empty-fld')
        }, 2000);
    } else if (_objectRegister.last_name.value == '') {
        _objectRegister.last_name.parentElement.classList.add('empty-fld');
        _objectRegister.last_name.focus();
        setTimeout(function() {
            _objectRegister.last_name.parentElement.classList.remove('empty-fld')
        }, 2000);
    }  else if (_objectRegister.za_id_number.value == '') {
        _objectRegister.za_id_number.parentElement.classList.add('empty-fld');
        _objectRegister.za_id_number.focus();
        setTimeout(function() {
            _objectRegister.za_id_number.parentElement.classList.remove('empty-fld')
        }, 2000);
    } else if (_objectRegister.password1.value == '') {
        _objectRegister.password1.focus()
    } else if (_objectRegister.password2.value == '') {
        _objectRegister.password2.parentElement.classList.add('empty-fld');
        _objectRegister.password2.focus();
        setTimeout(function() {
            _objectRegister.password2.parentElement.classList.remove('empty-fld')
        }, 2000);
    } else if (_objectRegister.password2.value != _objectRegister.password1.value) {
        _objectRegister.password2.parentElement.classList.add('pswdntmtch');
        _objectRegister.password2.focus();
        setTimeout(function() {
            _objectRegister.password2.parentElement.classList.remove('pswdntmtch')
        }, 2000);
    } else {
        registerConfirmbox.style.display = 'block';
        registerButton.submit.focus();
        _objectRegister.password2.blur();
        registerButton.register.style.display = 'none'
    }
})

registerButton.submit.addEventListener('focus', function() {
    document.addEventListener('keydown', function(event) {
        const key = event.key; // 'ArrowRight', 'ArrowLeft'
        switch (key) { // change to event.key to use the above variable etc.
            case 'ArrowLeft':
                // Left pressed
                event.preventDefault();
                registerButton.submit.focus();
                break;
                case 'ArrowRight':
                // Right pressed
                event.preventDefault();
                registerButton.cancel.focus();
                break;
        }
    })
})

// document.addEventListener('DOMContentLoaded', function() {
//     document.addEventListener('keydown', function(event) {
//         const key = event.key; // 'ArrowRight', 'ArrowLeft'
//         switch (key) { // change to event.key to use the above variable etc.
//             case 'ArrowLeft':
//                 // Left pressed
//                 event.preventDefault();
//                 registerButton.submit.focus();
//                 break;
//                 case 'ArrowRight':
//                 // Right pressed
//                 event.preventDefault();
//                 registerButton.cancel.focus();
//                 break;
//         }
//     })
// })

registerButton.cancel.addEventListener('click', function() {
    document.getElementById('registerConfirmbox').style.display = 'none';
    registerButton.register.style.display = 'block';
    _arrayRegister[0].focus()
})

// hide Register confirm box on input focus
_arrayRegister.forEach(function(item, index) {
    item.addEventListener('focus', function() {
        registerButton.register.style.display = 'block'
    })
})

function goBack() {
    window.history.back();
    setTimeout(location.reload(), 0)
}

// login 

//Login form array list
const _arrayLogin = [
    document.forms['loginForm']['username'], // login[0]
    document.forms['loginForm']['password'], // login[1]
]

// Shows one page and hides the other
// function showPage(page) {
//     document.querySelectorAll('div.task').forEach(div => {
//         div.style.display = 'none';
//     });
//     document.querySelector(`#${page}`).style.display = 'block';
//     if ( page == 'register') {
//         _arrayRegister[0].focus()
//     }
//     else if ( page == 'login') {
//         _arrayLogin[0].focus()
//     }
// }

// document.addEventListener('DOMContentLoaded', function() {
//     document.querySelectorAll('button.navB').forEach(button => {
//         button.onclick = function() {
//             showPage(this.dataset.page);
//         }
//     })
// });
