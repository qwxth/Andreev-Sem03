package main

func main() {
	a := GunStruct{true, 4, 4}
	*testStruct := &a
}

type GunStruct struct {
	On    bool
	Ammo  int
	Power int
}

func (c *GunStruct) Shoot() bool {
	if c.Ammo >= 1 && c.On != false {
		c.Ammo--
		return true
	}
	return false
}

func (c *GunStruct) RideBike() bool {
	if c.Power >= 1 && c.On != false {
		c.Power--
		return true
	}
	return false
}
