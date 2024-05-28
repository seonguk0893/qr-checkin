console.clear();

// 로그인 폼과 회원가입 폼 사이 전환 (클릭 이벤트 통한 슬라이드 업/다운 애니메이션)
const loginBtn = document.getElementById("login");
const signupBtn = document.getElementById("signup");

loginBtn.addEventListener("click", () => {
  const signupForm = document.querySelector(".signup");
  const loginForm = document.querySelector(".login");

  if (!signupForm.classList.contains("slide-up")) {
    signupForm.classList.add("slide-up");
    loginForm.classList.remove("slide-up");
  }
});

signupBtn.addEventListener("click", () => {
  const signupForm = document.querySelector(".signup");
  const loginForm = document.querySelector(".login");

  if (!loginForm.classList.contains("slide-up")) {
    loginForm.classList.add("slide-up");
    signupForm.classList.remove("slide-up");
  }
});
