package main

import (
    "strconv"
    "fmt"
    "github.com/garyburd/twister/server"
    "github.com/garyburd/twister/web"
)

func ServeHTTP(req *web.Request) {
    s := req.Param.Get("txt")
    ni, _ := strconv.Atoi(req.Param.Get("num"))
    wr := req.Respond(web.StatusOK)
    for i := 0; i < ni; i++ {
        fmt.Fprintf(wr, "%d: %s\n", i, s)
    }
}

func main() {
    router := web.NewRouter().
        Register("/<txt>/<num:[0-9]+>", "GET", ServeHTTP)
    server.Run(":8080", router)
}

