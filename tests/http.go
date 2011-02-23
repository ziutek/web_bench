package main

import (
    "http"
    "regexp"
    "strconv"
    "fmt"
)

type Handler struct {
    *regexp.Regexp
}

func (h *Handler) ServeHTTP(wr http.ResponseWriter, req *http.Request) {
    match := h.FindStringSubmatch(req.URL.Path)
    if req.Method != "GET" || match == nil {
        http.Error(wr, "Not found", 404)
        return
    }
    s := match[1]
    n, _ := strconv.Atoi(match[2])
    for i := 0; i < n; i++ {
        fmt.Fprintf(wr, "%d: %s\n", i, s)
    }
}

func main() {
    h := Handler{regexp.MustCompile("^/([^/]+)/([0-9]+)$")}
    http.ListenAndServe(":8080", &h)
}
