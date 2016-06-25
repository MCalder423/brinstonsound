using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace manager_mvc.Models
{
    public class Sound
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Location { get; set; }
        int Volume { get; set; }
        int Balance { get; set; }
        int Fade { get; set; }
    }
}
