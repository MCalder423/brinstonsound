using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net.Http.Headers;
using Newtonsoft.Json;

namespace manager.Models
{
    public class Sound
    {
        private string Host = Environment.GetEnvironmentVariable("AirhornDB_URL");

        public Guid SoundId { get; set; }
        public string Name { get; set; }
        public string Location { get; set; }
        int Volume { get; set; }
        int Balance { get; set; }
        int Fade { get; set; }

        public Sound()
        {

        }

        public async Task Load(Guid id)
        {
            var httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("MyClient", "1.0"));
            // Get the json string
            var result = await httpClient.GetStringAsync(String.Format("{0}/sounds/{1}", Host, id));
            // Parse it into a Sound Object
            Sound s = (Sound)JsonConvert.DeserializeObject(result);
            this.Balance = s.Balance;
            this.Fade = s.Fade;
            this.Location = s.Location;
            this.Name = s.Name;
            this.SoundId = s.SoundId;
            this.Volume = s.Volume;
        }

    }
}
