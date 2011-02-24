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

func usage() {
    fmt.Printf("Usage: %s {http|fcgi|scgi} ADDRESS\n", os.Args[0])
    os.Exit(1)
}

func main() {
    if len(os.Args) != 3 {
        usage()
    }
    proto := os.Args[1]
    addr := os.Args[2]

    web.Get("^/([^/]+)/([0-9]+)$", ServeHTTP)
    // Disable logging to minimize overhead
    web.SetLogger(log.New(&DevNull{}, "", 0))

    switch proto {
    case "http":
        web.Run(addr)
    case "fcgi":
        web.RunFcgi(addr)
    case "scgi":
        web.RunScgi(addr)
    default:
        usage()
    }
}


type DevNull struct {}
func (*DevNull) Write(p []byte) (int, os.Error) {
    return len(p), nil
}

