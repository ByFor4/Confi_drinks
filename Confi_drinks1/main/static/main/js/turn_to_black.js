function theme() {
    const blackTurn = document.querySelector('.black-turn')
    let el = document.documentElement

    blackTurn.addEventListener('click', () => {
        if(el.hasAttribute('black-on')){
            el.removeAttribute('black-on')
            localStorage.removeItem('theme')

        } else {
            el.setAttribute('black-on', 'dark')
            localStorage.setItem('theme', 'dark')
        }
        
    })

    if(localStorage.getItem('theme') !== null){
        el.setAttribute('black-on', 'dark')
    }
}

theme()

function nightTheme() {
    document.getElementById('black-turn1').style.transition ='background-color .5s ease-in-out 1s';
    document.getElementById('black-turn2').style.transition ='background-color .5s ease-in-out 1s';
    document.getElementById('black-turn3').style.transition ='background-color .5s ease-in-out 1s';
    document.getElementById('black_curtain').style.height ='100%';
    const timeoutId = setTimeout(darkTheme,1500);
    function darkTheme(){
        document.getElementById('black_curtain').style.height ='0px';
        // clearTimeout(timeoutId);
    }
}
