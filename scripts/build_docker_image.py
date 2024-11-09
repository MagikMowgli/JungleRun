import subprocess 
import sys 
import os 


def build_docker_image():
    try:
        print("Building Docker image...")  

        root_dir = "/home/mahdi/Desktop/JungleRun/JungleRun"  
        dockerfile_path = os.path.join(root_dir, "Dockerfile")  

     
        if not os.path.exists(dockerfile_path):
            print(f"Error: Dockerfile not found at {dockerfile_path}")
            sys.exit(1)

        # subprocess library allows us to run terminal commands in a python script 
        result = subprocess.run(
            ["docker", "build", "-t", "jungle_run_image", "-f", dockerfile_path, root_dir],
            check=True,  
            stdout=subprocess.PIPE,  # Capture the standard output 
            stderr=subprocess.PIPE   # Capture standard error 
        )
       
        print(result.stdout.decode()) 
        print("Docker image built successfully!")


    except subprocess.CalledProcessError as e:
        print(f"Error building Docker image: {e.stderr.decode()}", file=sys.stderr)
        sys.exit(1)  


if __name__ == "__main__":
    build_docker_image()  
