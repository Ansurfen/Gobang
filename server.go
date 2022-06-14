package main

import (
	"encoding/json"
	"fmt"
	"net"
	"strings"
)

type room struct {
	conns          []net.Conn
	play1_online   bool
	play2_online   bool
	play1_position []string
	play2_position []string
	count          int
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
				conns:          []net.Conn{play1, play2},
				play1_online:   true,
				play2_online:   true,
				play1_position: make([]string, 10),
				play2_position: make([]string, 10),
				count:          0})
			fmt.Println("Create a room...")
		}
	}
}

func Handler(r *room) {
	defer r.conns[0].Close()
	defer r.conns[1].Close()
	for {
		buf := make([]byte, 1024)
		if r.count%2 == 1 {
			n, err := r.conns[0].Read(buf)
			Panic(err)
			data := buf[:n]
			i := strings.IndexByte(string(data), ')')
			Broadcast(r, string(data[:i+1]))
		} else if r.count%2 == 0 {
			n, err := r.conns[1].Read(buf)
			Panic(err)
			data := buf[:n]
			i := strings.IndexByte(string(data), ')')
			Broadcast(r, string(data[:i+1]))
		}
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
	fmt.Println(string(json_bytes))
	r.conns[0].Write(json_bytes)
	r.conns[1].Write(json_bytes)
	r.count++
}

func Panic(err error) {
	if err != nil {
		panic(err.Error())
	}
}
