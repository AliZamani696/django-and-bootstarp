   let btns = document.querySelectorAll(".a")
      btns.forEach((p)=>{
        p.addEventListener("click",i=>{
            console.log(p.textContent)
        })
      })