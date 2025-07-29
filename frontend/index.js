const toggleTheme = async () => {
    const icon = document.getElementById("theme");
    const result = await chrome.storage.sync.get("theme");
    const currentTheme = result.theme ? result.theme : "light";
    const newTheme = currentTheme === "dark" ? "light" : "dark";

    if (newTheme === "dark") {
        icon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';
    } else {
        icon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>';
    }
    await chrome.storage.sync.set({ theme: newTheme });
}

document.addEventListener("DOMContentLoaded", () => {
    const icon = document.getElementById("theme");
    
    chrome.storage.sync.get("theme").then((result) => {
        const theme = result.theme || "light";
        if (theme === "dark") {
            icon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';
        } else {
            icon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>';
        }
    });

    icon.addEventListener("click", toggleTheme);
});


// get main content of page
const getMainContent = async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    const result = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
            const mainElement = document.querySelector("main");
            return mainElement ? mainElement.innerText : document.body.innerText;
        },
    });

    return result[0].result;
}

// inject main tag content with blurred text
const toggleBlur = async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: () => {
            // get the main element
            const mainElement = document.querySelector("main") || document.body;
            
            // add style based on the current state
            if (mainElement.classList.contains("blurred")) {
                mainElement.classList.remove("blurred");
                mainElement.style.userSelect = "auto";
                mainElement.style.pointerEvents = "auto";
                mainElement.style.filter = "none";
            } else {
                mainElement.classList.add("blurred");
                mainElement.style.userSelect = "none";
                mainElement.style.pointerEvents = "none";
                mainElement.style.filter = "blur(4px)";
            }
        }
    });

    return 0;
}

document.getElementById("refresh").addEventListener("click", toggleBlur);

document.getElementById("generate").addEventListener("click", async () => {
    const mainContent = await getMainContent();
    const mainTag = await toggleBlur();

    // disable click event to prevent multiple requests
    const generateButton = document.getElementById("generate");
    generateButton.disabled = true;
    generateButton.innerText = "G";

    const response = await fetch("http://localhost:8000/api/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            content: mainContent,
            token: "" 
        })
    }).then(res => res.json())
      .catch(err => console.error("Error:", err));

    console.log("Response:", response);
});
