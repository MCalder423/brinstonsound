using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace manager_mvc.Models
{
    public class Scheme_Sound
    {
        //public string Id { get; set; }
        public string SchemeId { get; set; }
        public string SoundId { get; set; }
        public string Name { get; set; }
        public string Type { get; set; }
        public int SwitchNumber { get; set; }
        public int Volume { get; set; }
        public int Balance { get; set; }
        public int Fade { get; set; }
        public int MinInterval { get; set; }
        public int MaxInterval { get; set; }
    }
}
