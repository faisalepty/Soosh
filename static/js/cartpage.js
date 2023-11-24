const decreaseQbtn = document.querySelectorAll('.Qdecrease');
const increaseQbtn = document.querySelectorAll('.Qincrease');
const qInputValue = document.querySelectorAll('.Qinput');

decreaseQbtn.forEach((btn) => {
  btn.addEventListener('click', (e) => {
    let i = btn.nextElementSibling.value
    const itemId1 = btn.nextElementSibling.getAttribute('id')
    const totalPrice1 = btn.parentElement.parentElement.parentElement.lastElementChild
    const grandTotal = document.getElementById('grandTotal')
    const subtotal = document.getElementById('subtotal')
    if(i > 1){
      i--
      btn.nextElementSibling.value = i
    }
    $.ajax({
      type: 'GET',
      url: `/addIcount/${itemId1}/`,
      data: {'quantity': i},
      header: {'X-Requested-With': 'XMLHttpRequest'},
      success: (res) => {
        if (totalPrice1.getAttribute('class') === 'totalPrice') {
          totalPrice1.innerText = `$${res.ucartItem.total.toFixed(1)}`
     }else{
      const totalPrice2 = btn.parentElement.parentElement.parentElement.parentElement.lastElementChild
      if (totalPrice2.getAttribute('class') === 'totalPrice'){
        totalPrice2.innerText = `$${res.ucartItem.total.toFixed(1)}`
      }
    }
    grandTotal.innerText = `$${res.ucartItem.grandTotal}`
    subtotal.innerText = `$${res.ucartItem.grandTotal}`
    console.log(res)

      },
      error: (res) => {
        console.log(res)
      },

    })
  })
})
increaseQbtn.forEach((btn) => {
  btn.addEventListener('click', (e) => {
      let x = btn.previousElementSibling.value
      const itemId = btn.previousElementSibling.getAttribute('id')
      const totalPrice = btn.parentElement.parentElement.parentElement.lastElementChild
      const grandTotal = document.getElementById('grandTotal')
      const subtotal = document.getElementById('subtotal')
      if(x < 100){
        x++
        btn.previousElementSibling.value = x
      }
      $.ajax({
        type: 'GET',
        url: `/addIcount/${itemId}/`,
        data: {'quantity': x},
        header: {'X-Requested-With': 'XMLHtmlrequest'},
        success: (res) => {
         if (totalPrice.getAttribute('class') === 'totalPrice') {          
            totalPrice.innerText = `$${res.ucartItem.total.toFixed(1)}`
        }else{
          const totalPrice2 = btn.parentElement.parentElement.parentElement.parentElement.lastElementChild
          if (totalPrice2.getAttribute('class') === 'totalPrice'){
            totalPrice2.innerText = `$${res.ucartItem.total.toFixed(1)}`
          }
        }
        grandTotal.innerText = `$${res.ucartItem.grandTotal}`
        subtotal.innerText = `$${res.ucartItem.grandTotal}`
        console.log(res)
        },
        error: (res) => {
          console.log(res)
        },
  
      })
  })
})