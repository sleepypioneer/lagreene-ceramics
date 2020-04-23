
var lightboxDescription = GLightbox({
    selector: 'glightbox'
  });

const showItem = (item) => {
    item.classList.remove('d-none');
    item.classList.add('fadeIn','glightbox');
  }

const hideItem = (item) => {
    item.classList.add('d-none');
    item.classList.remove('fadeIn','glightbox');
}

const clean = () => {
    const items = Array.from(document.getElementsByClassName("filter"));
    items.map(function (item, index) {
        item.classList.remove('fadeIn');
    })
}

  
  
function call(id) {
    const items = Array.from(document.getElementsByClassName("filter"));
    items.map(function (item, index) {
        if (id === "all") {
            if (item.classList.contains('archive')){
                hideItem(item);
            } else {
                showItem(item)
            }
            setTimeout(clean,500);
        } else if (id === "archive") {
            const check = item.classList.contains(id);
            if (check) {
                showItem(item)
            } else {
                hideItem(item)
            }
        } else {
            const check = item.classList.contains(id);
            if (check && !item.classList.contains('archive')) {
                showItem(item)
            } else {
                hideItem(item)
            }
        }
    })
}
