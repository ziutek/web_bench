package main

import (
    "os"
    "log"
    "strconv"
    "fmt"
    "github.com/hoisie/web.go"
)

func ServeHTTP(wr *web.Context, s, n string) {
    ni, _ := strconv.Atoi(n)
    for i := 0; i < ni; i++ {
        fmt.Fprintf(wr, "%d: %s\n", i, s)
    }
}

func main() {
    web.Get("^/([^/]+)/([0-9]+)$", ServeHTTP)
    // Disable logging to minimize overhead
    web.SetLogger(log.New(&DevNull{}, "", 0))
    web.Run(":8080")
}


type DevNull struct {}
func (*DevNull) Write(p []byte) (int, os.Error) {
    return len(p), nil
}

