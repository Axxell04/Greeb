const nameProject = document.querySelector(".name-project")
const descriptionProject = document.querySelector(".description-project")

const btnNext = document.querySelector(".btn-next")
const btnPrevius = document.querySelector(".btn-previus")

const mainImg = document.querySelector(".main-img")

// const otherImgs = Array.from(document.querySelector(".container-other-img").children)


// console.log(mainImg.src)

btnNext.addEventListener("click", () => {
    nextImg();
})

btnPrevius.addEventListener("click", () => {
    previusImg();
})

const URLServer = window.location.origin
console.log(URLServer)

const projectID = 1
let projectImgs = []
let actualImgID = 1

const getProjects = async () => {
    const res = await fetch(`${URLServer}/api/get_projects`)
    const data = await res.json()
    console.log(data)
    printProyect(data)
}

getProjects()

const printProyect = (data) => {
    data.map((project) => {
        if (project.id === projectID) {
            nameProject.textContent = project.name;
            descriptionProject.textContent = project.description;
            mainImg.src = project.imgs[0].src;
            projectImgs = project.imgs;
        }
    })
}

const changeImgSrc = () => {
    projectImgs.map((img) => {
        if (img.id === actualImgID) {
            mainImg.src = img.src;
        }
    })
}

const nextImg = () => {
    let imgLength = projectImgs.length
    if (actualImgID + 1 <= imgLength) {
        actualImgID++;
    } else {
        actualImgID = 1;
    }
    changeImgSrc();
}

const previusImg = () => {
    if (actualImgID - 1 >= 1) {
        actualImgID--;
    } else {
        actualImgID = projectImgs.length;
    }
    changeImgSrc();
}