const addToCartIcon = document.querySelectorAll('.addToCartIcon');
const cartCount = document.querySelectorAll('.cartCount');
addToCartIcon.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    e.preventDefault()
      const itemId = btn.getAttribute('id');
  $.ajax({
        type: 'GET',
        url: `/addToCart/${itemId}/`,
        headers: {'X-Requested-With': 'XMLHttpRequest'}, 
        success: function (res) {
            cartCount.forEach( icon => {
              let x = parseInt(icon.innerText);
              x++;
              icon.innerText = x
            })
            console.log(res)
        },
        error: (res) => (
          console.log(res.error)
        )
      })
    })
      
  })