package main

import (
	"encoding/json"
	"log"
	"net"
	"strings"
)

type room struct {
	conns []net.Conn
	count int
}

type SyncInfo struct {
	Count int    `json:"count"`
	Play1 string `json:"play1"`
	Play2 string `json:"play2"`
}

func main() {
	server, err := net.Listen("tcp", ":8080")
	Panic(err)
	conns := make(chan net.Conn, 20)
	for {
		conn, err := server.Accept()
		Panic(err)
		conns <- conn
		if len(conns) >= 2 {
			play1 := <-conns
			play2 := <-conns
			go Handler(&room{
				conns: []net.Conn{play1, play2},
				count: 0})
			log.Println("Create a room...")
		}
	}
}

func Handler(r *room) {
	defer r.conns[0].Close()
	defer r.conns[1].Close()
	for {
		buf := make([]byte, 1024)
		var n int
		if r.count%2 == 1 {
			n, _ = r.conns[0].Read(buf)
		} else if r.count%2 == 0 {
			n, _ = r.conns[1].Read(buf)
		}
		data := buf[:n]
		i := strings.IndexByte(string(data), ')')
		Broadcast(r, string(data[:i+1]))
	}
}

func Broadcast(r *room, data string) {
	if len(data) == 0 {
		return
	}
	info := SyncInfo{Count: r.count}
	if r.count%2 == 0 {
		info.Play2 = data
	} else if r.count%2 == 1 {
		info.Play1 = data
	}
	json_bytes, err := json.Marshal(info)
	Panic(err)
	log.Println(string(json_bytes))
	r.conns[0].Write(json_bytes)
	r.conns[1].Write(json_bytes)
	r.count++
}

func Panic(err error) {
	if err != nil {
		panic(err.Error())
	}
}
