var swiper = new Swiper('.swiper-container', {
  effect: 'coverflow',
  slidesPerView: 'auto',
  spaceBetween: 10,
  centeredSlides: true,
  grabCursor: true,
  loop: true,
  coverflowEffect: {
      rotate: 40,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows : true,
  },
  pagination: {
      el: '.swiper-pagination',
      clickable: true,
  },
  navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
  },
});