const productCounter = () =>{
    let productsCount = document.querySelectorAll(".product-active").length;
    let productsCountSpan = document.getElementById('products_count');
    if(productsCount == 0){
        productsCountSpan.innerText = "لا يوجد منتجات";
        document.querySelector('.total-products').style = "justify-content: center;";
    }
    else if(productsCount == 1){
        productsCountSpan.innerText = productsCount + ' ' + 'منتج';
        document.querySelector('.total-products').style = "";
    }
    else{
        productsCountSpan.innerText = productsCount + ' ' +'منتجات';
        document.querySelector('.total-products').style = "";
    }
  }
  window.addEventListener('load', () => {
    productCounter();
  });
  
  const searchInput = document.getElementById('search');
  
  searchInput.addEventListener('input', () => {
    const filterValue = searchInput.value.trim().toLowerCase();
  
    const products = document.querySelectorAll('.product');
    products.forEach((product) => {
      const productName = product.querySelector('.product-name').textContent.trim().toLowerCase();
  
      if (productName.includes(filterValue)) {
        product.classList.remove('hide');
        product.classList.add('product-active');
      } else {
        product.classList.add('hide');
        product.classList.remove('product-active');
      }
      productCounter();
    });
  });