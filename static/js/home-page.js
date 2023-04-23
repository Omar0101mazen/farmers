// swiper
var mySwiper = new Swiper('.swiper-container', {
    effect: '',
    loop: true,
    speed: 1000,
    slidesPerView: 1,
    autoplay: {
        delay: 5000,
      },
    navigation: {
       nextEl: '.swiper-button-next',
       prevEl: '.swiper-button-prev'
    },
    pagination: {
       el: '.swiper-pagination',
       type: 'bullets',
       clickable: 'true'
    },
 });

//hero

let slider = document.querySelector(".swiper-container");
let headerHeight = document.querySelector(".header").offsetHeight;
slider.style.height = (window.innerHeight - headerHeight) +"px";

let nameAndWork = {
    adham : "Programmer",
    omar : "Py Developer",
    ali : "php Developer",

    meth : ()=>{
        console.log(`hello your work is ${nameAndWork.adham} Thank You`)
    }
}
